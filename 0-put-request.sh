#!/bin/bash
set -v

curl -X PUT https://ne9wy64v12.execute-api.eu-central-1.amazonaws.com/Prod/text -d '{"text":"Such a great movie!"}'
