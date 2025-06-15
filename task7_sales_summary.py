import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect('sales_data.db')

# Run SQL query
query = '''
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product
'''
df = pd.read_sql_query(query, conn)
conn.close()

# Print the result
print(df)

# Plot bar chart
df.plot(kind='bar', x='product', y='revenue', legend=False, title='Revenue per Product')
plt.ylabel('Revenue')
plt.tight_layout()
plt.savefig('sales_chart.png')
plt.show()
