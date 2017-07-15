create table user(
    id int not null auto_increment primary key,
    user varchar(50) not null,
    password varchar(200) not null,
    type varchar(10)
)



create table idc(
    id int not null auto_increment primary key,
    name varchar(50) not null,
    mobile varchar(20) not null
)