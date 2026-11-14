-- Read-only user for QueryPilot (local practice password only)
CREATE ROLE qp_reader LOGIN PASSWORD 'reader_pw';

-- Allow it to connect to the northwind database and see the public schema
GRANT CONNECT ON DATABASE northwind TO qp_reader;
GRANT USAGE ON SCHEMA public TO qp_reader;

-- Allow reading (SELECT) every table, and nothing else
GRANT SELECT ON ALL TABLES IN SCHEMA public TO qp_reader;

-- Extra safety: every session is read-only and queries stop after 5 seconds
ALTER ROLE qp_reader SET default_transaction_read_only = on;
ALTER ROLE qp_reader SET statement_timeout = '5s';

