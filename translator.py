import re
import textwrap
from openai_client import get_openai_client

# A concise description of the database schema
SCHEMA = textwrap.dedent("""
Tables:
  runners(runner_id INT PK, name VARCHAR, age TINYINT)
  races(race_id INT PK, name VARCHAR, date DATE, location VARCHAR, distance_km DECIMAL)
  race_results(result_id INT PK, runner_id INT FK→runners, race_id INT FK→races,
               bib_number VARCHAR, finish_time_sec INT, finish_rank INT)
""")

def translate_nl_to_sql(nl_request):
    """Return a single SQL statement (string) for the user's request."""

    client = get_openai_client()

    prompt = textwrap.dedent(f"""
        You are an expert SQL assistant. The schema for the MySQL database `chatdb` is:

        {SCHEMA}

        Output exactly one valid MySQL SQL statement—no comments, no explanations, no markdown.
        Use standard SQL keywords (SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY, LIMIT, OFFSET).

        User request:
        {nl_request}

        Only output the SQL statement.
    """)

    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": prompt}]
    )

    sql = resp.choices[0].message.content.strip()
    return sql