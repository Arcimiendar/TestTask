echo "SELECT 'CREATE DATABASE calc_test' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'calc_test')\\gexec" | psql -U calc
