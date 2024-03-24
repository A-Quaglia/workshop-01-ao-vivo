create table vendas(
	id SERIAL primary key,
	email varchar(255) not NULL,
    data timestamp not NULL,
    valor numeric(10, 2) not null check (valor>=0),
    produto integer not null check (valor>=0),
    quantidade varchar(255) not null,
    categoria varchar(50) not null
);