select
    "Status",
    count("id"),
    avg("nb_year_employment"::float) as "avg_year_of_employment"
-- double-dash is a way to comment in SQL
-- below, you should replace YOUR_PROJECT by the KEY of your project, available in the url in uppercase
from "YOUR_PROJECT_customer_information_copy"
group by "Status"

