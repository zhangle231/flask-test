import psyconpg2
import psycopg2
conn = psycopg2.connect("dbname=test user=zl")
cur = conn.cursor()
cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
conn.commit()
cur.execute('''
CREATE FUNCTION insert_test(subtotal real) RETURNS real AS $$
BEGIN
   insert into test values(1,1,'1');
END;
$$ LANGUAGE plpgsql;
''')
conn.commit()
cur.execute('''
CREATE FUNCTION insert_test(subtotal real) RETURNS real AS $$
BEGIN
   insert into test values(1,1,'1');
   return 0;
END;
$$ LANGUAGE plpgsql;
''')
conn.comit()
conn.commit()
cur.execute('''
CREATE FUNCTION insert_test2(subtotal real) RETURNS real AS $$
BEGIN
   insert_test(1);
   return 0;
END;
$$ LANGUAGE plpgsql;
''')
cur.execute('''
CREATE FUNCTION insert_test2(subtotal real) RETURNS real AS $$
BEGIN
   select insert_test(1);
   return 0;
END;
$$ LANGUAGE plpgsql;
''')
cur.execute('''
CREATE FUNCTION insert_test2(subtotal real) RETURNS real AS $$
BEGIN
   select insert_test(1);
   return 0;
END;
$$ LANGUAGE plpgsql;
''')
cur = conn.cursor()
cur.execute('''
CREATE FUNCTION insert_test2(subtotal real) RETURNS real AS $$
BEGIN
   select insert_test(1);
   return 0;
END;
$$ LANGUAGE plpgsql;
''')
conn = psycopg2.connect("dbname=test user=zl")
cur = conn.cursor()
cur.execute('''
CREATE FUNCTION insert_test2(subtotal real) RETURNS real AS $$
BEGIN
   select insert_test(1);
   return 0;
END;
$$ LANGUAGE plpgsql;
''')
cur.commit()
conn.commit()
cur.execute('''
CREATE FUNCTION insert_test2(subtotal real) RETURNS real AS $$
BEGIN
   PERFORM insert_test(1);
   return 0;
END;
$$ LANGUAGE plpgsql;
''')
conn.commit()
cur.execute("select insert_test2(1)")
conn.commit()
cur.execute("select insert_test2(1)")
conn.rollback()
conn.commit()
?
_i17
help
help()
help
help()
?
%hist -f tmp.py
