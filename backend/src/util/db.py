import os
import psycopg2
import uuid

DATABASE_URL = os.getenv("DATABASE_URL")

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

cursor = conn.cursor()

def create_users_table():
    sql = """
        CREATE TABLE IF NOT EXISTS Users (
            id varchar(255) NOT NULL PRIMARY KEY
        );
    """

    try:
        cursor.execute(sql)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def create_portfolios_table():
    sql = """ CREATE TABLE IF NOT EXISTS public.Portfolios (
    id varchar(255) NOT NULL PRIMARY KEY,
    user_id varchar(255) NOT NULL,
    name varchar(255) NOT NULL
    ) """
    
    try:
        cursor.execute(sql)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def create_purchases_table():
    sql = """ CREATE TABLE IF NOT EXISTS public.Purchases (
    id varchar(255) NOT NULL PRIMARY KEY,
    portfolio_id varchar(255) NOT NULL,
    coin_id varchar(255) NOT NULL,
    time_of_purch timestamp without time zone NOT NULL,
    purch_price float NOT NULL,
    amount_bought float NOT NULL
    ) """
    
    try:
        cursor.execute(sql)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def create_orders_table():
    sql = """ CREATE TABLE IF NOT EXISTS public.Orders (
    id varchar(255) NOT NULL PRIMARY KEY,
    portfolio_id varchar(255) NOT NULL,
    coin_id varchar(255) NOT NULL,
    time_of_purch timestamp without time zone NOT NULL,
    amount_bought float NOT NULL
    ) """
    
    try:
        cursor.execute(sql)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def create_watched_table():
    sql = """ CREATE TABLE IF NOT EXISTS public.Watching (
    id varchar(255) NOT NULL PRIMARY KEY,
    portfolio_id varchar(255) NOT NULL,
    coin_id varchar(255) NOT NULL
    ) """
    
    try:
        cursor.execute(sql)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# WATCHLIST

def get_watchlist(portfolio_id):
    sql = "SELECT * FROM public.Watching WHERE portfolio_id = %s"
    cursor.execute(sql, (portfolio_id,))
    return cursor.fetchall()


def post_watching(portfolio_id, coin_id):
    id = str(uuid.uuid4())
    try:
        cursor.execute("""
        INSERT INTO public.Watching (
        id,
        portfolio_id,
        coin_id
        ) VALUES (%s, %s, %s)""", (id, portfolio_id, coin_id))
        
        # commit the changes
        conn.commit()
        return id
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return "Failed to post Watchlist item"

def delete_watching(id):
    try:
        print(id)
        cursor.execute("""
        DELETE FROM public.Watching 
        WHERE id = ?
        """, (id))
        
        # commit the changes
        conn.commit()
        return id
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return "Failed to delete Watchlist item"

# PURCHASES

def get_purchases(portfolio_id):
    sql = "SELECT * FROM public.Purchases WHERE portfolio_id = %s"
    cursor.execute(sql, (portfolio_id,))
    return cursor.fetchall()

def post_purchase(portfolio_id, coin_id, time_of_purch, purch_price, amount_bought):
    try:
        cursor.execute("""
        INSERT INTO public.Watching (
        id,
        portfolio_id,
        coin_id,
        time_of_purch,
        purch_price,
        amount_bought
        ) VALUES (%s, %s, %s, %s, %s, %s)""", (str(uuid.uuid4()), portfolio_id, coin_id, time_of_purch, purch_price, amount_bought))
        
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# ORDERS

def get_orders(portfolio_id):
    sql = "SELECT * FROM public.Orders WHERE portfolio_id = %s"
    cursor.execute(sql, (portfolio_id,))
    return cursor.fetchall()
    

def post_order(portfolio_id, coin_id, time_of_purch, amount_bought):
    try:
        cursor.execute("""
        INSERT INTO public.Watching (
        id,
        portfolio_id,
        coin_id,
        time_of_purch,
        amount_bought
        ) VALUES (?, ?, ?, ?, ?, ?)""", (str(uuid.uuid4()), portfolio_id, coin_id, time_of_purch, amount_bought))
        
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def delete_order(id):
    try:
        cursor.execute("""
        DELETE FROM public.Orders 
        WHERE id = ?
        """, (id))
        
        # commit the changes
        conn.commit()
        return id
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return "Failed to delete order"

# PORTFOLIOS

def get_portfolios(user_id):
    sql = "SELECT * FROM public.Portfolios WHERE user_id = %s"
    cursor.execute(sql, (user_id,))
    return cursor.fetchall()

def post_portfolio(user_id, name):
    id = str(uuid.uuid4())
    try:
        cursor.execute("""
        INSERT INTO public.Portfolios (
        id,
        user_id,
        name
        ) VALUES (%s, %s, %s)""", (id, user_id, name))
        
        # commit the changes
        conn.commit()
        return id
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return "Failed to post Portfolio"