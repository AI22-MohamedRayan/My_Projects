from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("Bundesliga Analysis") \
    .getOrCreate()

# Load datasets into DataFrames
matches_df = spark.read.csv('Matches.csv', header=True, inferSchema=True)
teams_in_matches_df = spark.read.csv('Teams_in_Matches.csv', header=True, inferSchema=True)
teams_df = spark.read.csv('Teams.csv', header=True, inferSchema=True)
unique_teams_df = spark.read.csv('Unique_Teams.csv', header=True, inferSchema=True)

# Show schema and sample data for each DataFrame (optional)
matches_df.printSchema()
matches_df.show(5, truncate=False)

teams_in_matches_df.printSchema()
teams_in_matches_df.show(5, truncate=False)

teams_df.printSchema()
teams_df.show(5, truncate=False)

unique_teams_df.printSchema()
unique_teams_df.show(5, truncate=False)

# Example analysis: Count matches per team using appropriate column names
# Adjust column names based on actual schema of teams_in_matches_df
matches_per_team = teams_in_matches_df.groupBy('Unique_Team_ID').agg(count('Match_ID').alias('matches_count'))

matches_per_team.show()

# Perform further analysis as per your specific questions/tasks

# Stop SparkSession
spark.stop()
