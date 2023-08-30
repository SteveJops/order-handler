
#!/bin/bash

set -o errexit
set -o nounset

celery -A ordershandler worker -l INFO