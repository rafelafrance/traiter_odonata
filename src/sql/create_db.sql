drop table if exists guides;
create table guides (
    name   text primary key,
    path   text,
    date   text,
    method text,
    pdf    text
);
create index guides_date on guides (date);
