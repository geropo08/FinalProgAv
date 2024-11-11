class Consulta:
    def __init__(self, idioma, query=None):
            """
            Initializes the Consulta object.
            
            :param query: The SQL query string.
            :param idioma: idioma de la query.
            """
            if query is None:
                self.query = ""
            else:
                self.query=query
            self.idioma = idioma



    def nombre(self, nombre):
        self.query += nombre+" "
        return self
    def eq_op(self):
        self.query += "= "
        return self
    def gr_op(self):
        self.query += "> "
        return self
    def ls_op(self):
        self.query += "< "
        return self
    def ls_params(self, params):
        self.query += params+" "
        return self
    
    def select(self):
        self.query += "SELECT "
        return self
    
    def everything(self):
        self.query += "* "
        return self
    
    def from_table(self):
        self.query += "FROM "
        return self

    def where(self):
        self.query += "WHERE "
        return self

    def group_by(self):
        self.query += "GROUP BY "
        return self

    def join(self):
        self.query += "JOIN "
        return self

    def on(self):
        self.query += "ON "
        return self

    def distinct(self):
        self.query += "DISTINCT "
        return self

    def count(self):
        self.query += "COUNT "
        return self

    def insert_into(self):
        self.query += "INSERT INTO "
        return self

    def values(self):
        self.query += "VALUES "
        return self

    def update(self):
        self.query += "UPDATE "
        return self

    def set(self):
        self.query += "SET "
        return self

    def delete(self):
        self.query += "DELETE "
        return self

    def order_by(self):
        self.query += "ORDER BY "
        return self

    def limit(self):
        self.query += "LIMIT "
        return self

    def having(self):
        self.query += "HAVING "
        return self

    def exists(self):
        self.query += "EXISTS "
        return self

    def in_this(self):
        self.query += "IN "
        return self

    def between(self):
        self.query += "BETWEEN "
        return self

    def like(self):
        self.query += "LIKE "
        return self

    def is_null(self):
        self.query += "IS NULL "
        return self

    def alter_table(self):
        self.query += "ALTER TABLE "
        return self

    def add_column(self):
        self.query += "ADD COLUMN "
        return self

    def drop_column(self):
        self.query += "DROP COLUMN "
        return self

    def create_table(self):
        self.query += "CREATE TABLE "
        return self

    def drop_table(self):
        self.query += "DROP TABLE "
        return self

    def default(self):
        self.query += "DEFAULT "
        return self

    def unique(self):
        self.query += "UNIQUE "
        return self

    def primary_key(self):
        self.query += "PRIMARY KEY "
        return self

    def foreign_key(self):
        self.query += "FOREIGN KEY "
        return self

    def not_null(self):
        self.query += "NOT NULL "
        return self

    def cast(self):
        self.query += "CAST "
        return self

    def and_op(self):
        self.query += "AND "
        return self

    def or_op(self):
        self.query += "OR "
        return self

    def get_query(self):
        return self.query.strip()
    

   