-- 建表: 父表
CREATE TABLE `author` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
);


-- 建表: 子表
CREATE TABLE `article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `content` mediumtext NOT NULL,
  `author_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `author_id` (`author_id`),

  -- `author`表在这里被视为是`article`表的父表.
  -- ON DELETE CASCADE: `author`数据被删除时, 也会对应删除当前表关联的数据.
  FOREIGN KEY (`author_id`) REFERENCES `author` (`id`) ON DELETE CASCADE
);


-- 插入数据
insert into `author` (`name`) values ('zhang_san'), ('li_si'), ('lao_wang');
insert into `article` (`title`, `content`, `author_id`) values ('文章-1', '内容-1', '1');
insert into `article` (`title`, `content`, `author_id`) values ('文章-2', '内容-2', '1');
commit;


-- 测试: 删除 `author`.`id` = 1 的数据
delete from `author` where id=1;


-- 断言: 确认 `article` 表中的'文章-1' 和 '文章-2' 这两条数据也被删除了.
select * from `article`;


-- 恢复: 删除表 `author` 和 `article`
delete from `article`;		-- 先清空子表
delete from `author`;       -- 再清空父表
drop table `article`;       -- 先删除子表(referencing table)
drop table `author`;        -- 再删除父表(referenced table)


-- 备注:
-- 删除一条父表中的数据, 数据库会自动同步的删除子表(关联表)中的关联数据(可以是一条, 也可以是多条).
-- 但需要注意的是, 数据库不允许直接清空父表的数据.
