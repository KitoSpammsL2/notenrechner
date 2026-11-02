#!/usr/bin/env bash
# Legt die Azure-Dienste für den Notenrechner in den Gratis-Stufen an.
# Voraussetzung: az login. Das Datenbank-Passwort wird erzeugt und nie angezeigt.
set -euo pipefail

RESOURCE_GROUP="${RESOURCE_GROUP:-notenrechner-rg}"
LOCATION="${LOCATION:-switzerlandnorth}"
PLAN="${PLAN:-notenrechner-plan}"
APP="${APP:-notenrechner-lb324}"
DB_SERVER="${DB_SERVER:-notenrechner-db-lb324}"
DB_NAME="${DB_NAME:-notenrechner}"
DB_USER="${DB_USER:-notenadmin}"

random_secret() {
  python -c "import secrets, string; a = string.ascii_letters + string.digits; print('Aa1' + ''.join(secrets.choice(a) for _ in range(29)))"
}

az provider register --namespace Microsoft.Web --wait
az provider register --namespace Microsoft.DBforPostgreSQL --wait

az group create --name "$RESOURCE_GROUP" --location "$LOCATION" --output none

az appservice plan create \
  --resource-group "$RESOURCE_GROUP" \
  --name "$PLAN" \
  --location "$LOCATION" \
  --is-linux \
  --sku F1 \
  --output none

az webapp create \
  --resource-group "$RESOURCE_GROUP" \
  --plan "$PLAN" \
  --name "$APP" \
  --runtime "PYTHON:3.13" \
  --output none

DB_PASS="$(random_secret)"

az postgres flexible-server create \
  --resource-group "$RESOURCE_GROUP" \
  --name "$DB_SERVER" \
  --location "$LOCATION" \
  --tier Burstable \
  --sku-name Standard_B1ms \
  --storage-size 32 \
  --version 17 \
  --zonal-resiliency Disabled \
  --geo-redundant-backup Disabled \
  --backup-retention 7 \
  --storage-auto-grow Disabled \
  --public-access 0.0.0.0 \
  --admin-user "$DB_USER" \
  --admin-password "$DB_PASS" \
  --yes \
  --output none

az postgres flexible-server db create \
  --resource-group "$RESOURCE_GROUP" \
  --server-name "$DB_SERVER" \
  --name "$DB_NAME" \
  --output none

az webapp config appsettings set \
  --resource-group "$RESOURCE_GROUP" \
  --name "$APP" \
  --settings \
  "DBHOST=$DB_SERVER.postgres.database.azure.com" \
  "DBNAME=$DB_NAME" \
  "DBUSER=$DB_USER" \
  "DBPASS=$DB_PASS" \
  "SECRET_KEY=$(random_secret)" \
  "SCM_DO_BUILD_DURING_DEPLOYMENT=true" \
  --output none

az webapp config set \
  --resource-group "$RESOURCE_GROUP" \
  --name "$APP" \
  --startup-file "gunicorn --bind=0.0.0.0 --timeout 600 main:app" \
  --output none

echo "Fertig: https://$(az webapp show --resource-group "$RESOURCE_GROUP" --name "$APP" --query defaultHostName --output tsv)"
