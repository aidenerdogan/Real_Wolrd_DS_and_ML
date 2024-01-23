# Divvy Bike Trip Generation and Visualization

- The objective of this project was to overcome the absence of trip data for the renowned Chicago Bike sharing service, Divvy. To achieve this, a custom solution was developed to generate trip data by capturing regular snapshots of the stations and the availability of bikes. The process involved pulling snapshots at a frequency of one per minute.

- The algorithm for trip generation was designed to identify instances where a bike moved from one station to another in a short period of time. When such a scenario was detected, it was considered as a trip and included in the generated data. This approach allowed for the reconstruction of historical trip information, enabling analysis and insights into user patterns and bike movements.

- A significant part of the project revolved around data wrangling, including cleaning and preprocessing the captured snapshots. Trips taken by staff members during system service and inspection, as well as trips with durations below 60 seconds (possibly indicating false starts or users attempting to re-dock a bike securely), were filtered out to ensure the accuracy and reliability of the generated trip data.

- One of the most enjoyable aspects of the project was the analysis and visualization of the generated trip data. The data was visualized on interactive folium maps, enabling clear and insightful representations of bike movements, popular routes, and other relevant patterns. This visualization component added depth and clarity to the analysis, making it easier to understand the dynamics of the bike sharing system and its usage patterns.

- Overall, this project successfully tackled the challenge of the lack of trip data for Divvy by implementing a custom trip generation approach. By leveraging regular snapshots and applying data wrangling techniques, accurate trip data was generated, allowing for comprehensive analysis and visualization on interactive folium maps.