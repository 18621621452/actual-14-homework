# 初始化表结构及数据

create table user(
username varchar(20) not null default '',
password varchar(20) not null default ''
)engine=innodb default charset=utf8;


insert into user values('admin','admin');
