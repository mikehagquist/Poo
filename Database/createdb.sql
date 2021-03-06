DROP DATABASE if exists rdb;
DROP USER if exists rdb;
CREATE USER rdb;
CREATE DATABASE rdb;
GRANT ALL PRIVILEGES ON DATABASE rdb TO rdb;

CREATE TABLE films (
    code        char(5) CONSTRAINT firstkey PRIMARY KEY,
    title       varchar(40) NOT NULL,
    did         integer NOT NULL,
    date_prod   date,
    kind        varchar(10),
    len         interval hour to minute
);

CREATE TABLE distributors (
     did    integer PRIMARY KEY DEFAULT nextval('serial'),
     name   varchar(40) NOT NULL CHECK (name <> '')
);