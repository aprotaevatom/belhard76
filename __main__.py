from psycopg2 import connect
from psycopg2.extras import NamedTupleCursor



# TODO host for windows 127.0.0.1 | localhost
# conn = connect("postgresql://admin:password@0.0.0.0:5432/bh")
# cur = conn.cursor()


with connect("postgresql://admin:password@0.0.0.0:5432/bh", cursor_factory=NamedTupleCursor) as conn:
    with conn.cursor() as cur:
        # cur.execute('CREATE SCHEMA IF NOT EXISTS catalog AUTHORIZATION admin;')  # создание схемы таблиц

        # cur.execute(
        #     query="""
        #         CREATE TABLE IF NOT EXISTS blog.users (
        #             id BIGSERIAL PRIMARY KEY,
        #             email VARCHAR (128) NOT NULL UNIQUE CHECK ( length(email) >= 5  AND email LIKE '%_@%_._%'),
        #             password CHAR ( 60 ) NOT NULL,
        #             profile_icon VARCHAR NOT NULL DEFAULT ( 'https://answers-afd.microsoft.com/static/images/image-not-found.jpg' ),
        #             is_active BOOLEAN NOT NULL DEFAULT (false)
        #         );
        #     """
        # )
        # cur.execute(
        #     query="""
        #         CREATE TaBlE IF not exists blog.posts (
        #             id bigserial primary key ,
        #             user_id BIGINT not null,
        #             title varchar (128) not null ,
        #             body varchar not null ,
        #             foreign key (user_id) references blog.users(id) on delete cascade on update cascade
        #         );
        #     """
        # )
        # cur.execute(
        #     query="""
        #         create table if not exists blog.categories (
        #             id smallserial primary key ,
        #             name varchar ( 32 ) not null unique check ( length(name) >= 2 )
        #         );
        #     """
        # )
        cur.execute(
            query="""
                create table if not exists blog.post_categories (
                    post_id bigint not null ,
                    category_id smallint not null ,
                    foreign key (post_id) references blog.posts(id) on delete cascade  on update cascade ,
                    foreign key (category_id) references blog.categories(id) on delete cascade  on update cascade ,
                    primary key (post_id, category_id)
                );
            """
        )

        # cur.execute(
        #     query="drop table blog.post_categories;"
        # )
        # cur.execute(
        #     query="alter table blog.post_categories drop column is_published;"
        # )
        # cur.execute(
        #     query="""
        #         alter table blog.posts
        #         add column is_published boolean not null default (false);
        #     """
        # )

        # cur.execute(
        #     query="alter table blog.categories alter column name type varchar(128);"
        # )

        # cur.executemany(
        #     query="insert into blog.categories (name) values (%(category_name)s);",
        #     params_seq=[
        #         {
        #             "category_name": "Auto"
        #         },
        #         {
        #             "category_name": "Moto"
        #         }
        #     ]
        # )

        # cur.execute(
        #     query=f"insert into blog.categories (name) values (%s);",
        #     params=[(input(),)]
        # )

        # cur.execute(
        #     query="""
        #         update blog.categories SET name = %s
        #         where lower(name) like 'new*';
        #     """,
        #     params=("New", )
        # )
        # cur.execute(query="select * from blog.categories where blog.categories.id IN (1, 2) ;")
        # print(cur.fetchall())

        # cur.execute(
        #     query="delete from blog.categories where id = 5;"
        # )

        # cur.execute(
        #     query="""
        #         select *
        #         from blog.categories
        #         order by blog.categories.name, blog.categories.id;
        #     """
        # )
        # print(cur.fetchall())

        # cur.execute("""
        # select round((sum(blog.categories.id) / min(blog.categories.id)) * 1.2, 3) as attr
        # from blog.categories;""")
        # cur.execute(
        #     query="""
        #         select * from blog.categories where id = (select min(blog.categories.id) from blog.categories where name like '%o%') ;
        #     """
        # )
        # print(cur.fetchall())

        # cur.execute(
        #     query="""
        #         insert into blog.posts (user_id, title, body, is_published)
        #         values (
        #         (select blog.users.id from blog.users where blog.users.email = 'vasya@gmail.com'),
        #         'title', 'body', true
        #         );
        #     """
        # )

        conn.commit()
