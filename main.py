import argparse
from translator import translate_nl_to_sql
from mysql_client import get_mysql_connection

def main():
    parser = argparse.ArgumentParser(
        description="Natural‑language interface to ChatDB (MySQL)"
    )
    parser.add_argument(
        "-q", "--query", required=True,
        help="Your natural‑language SQL request"
    )
    args = parser.parse_args()

    # Translate NL to SQL
    sql = translate_nl_to_sql(args.query)
    print("Generated SQL:\n" + sql + "\n")

    # Execute SQL
    conn = get_mysql_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)

    # Display results or affected rows
    if cursor.with_rows:
        rows = cursor.fetchall()
        if rows:
            # Print header and rows comma-separated
            cols = cursor.column_names
            print(", ".join(cols))
            for row in rows:
                print(", ".join(str(row[col]) for col in cols))
        else:
            print("No results found.")
    else:
        conn.commit()
        print(f"Rows affected: {cursor.rowcount}")

    # Cleanup
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
