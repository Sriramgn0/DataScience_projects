# Manifest

This directory contains the following data:

# snb-data-rendoblim-en-all-20170502_1430.csv

- Data: Yields on bond issues (Switzerland) by month, breakdown by term
- Source: https://data.snb.ch/en/topics/ziredev#!/cube/rendoblim
- Date published: 02 May 2017, 14:30

# snb-data-zimoma-en-all-20170502_1430.csv

- Data: Money market rates, breakdown by term and exchange
- Source: https://data.snb.ch/en/topics/ziredev#!/cube/zimoma
- Date published: 02 May 2017, 14:30

# mpg.csv

- Data: Car fuel efficiency
- Source: https://raw.githubusercontent.com/tidyverse/ggplot2/master/data-raw/mpg.csv

# burtin.json

- Data: Antibiotics Efficacy
- Source: https://mbostock.github.io/protovis/ex/antibiotics-burtin.html
- Import: pd.read_json('burtin.json', orient='records')

# API_NY

- Data: GDP growth %
- Source: http://data.worldbank.org/indicator/NY.GDP.MKTP.CD?locations=CH
- See also: https://en.wikipedia.org/wiki/Economy_of_Switzerland

# homog_mo_SMA.txt

- Data: Temperature in Zürich
- Source: http://www.meteoschweiz.admin.ch/product/output/climate-data/homogenous-monthly-data-processing/data/homog_mo_SMA.txt
- See also: http://www.meteoschweiz.admin.ch/home/klima/schweizer-klima-im-detail/homogene-messreihen-ab-1864.html?station=sma
- Date downloaded: 18 Jan 2018
- Import: pd.read_table('homog_mo_SMA.txt', sep="\s+", skip_blank_lines=False, header=27)

# anscombe.csv

- Data: Anscombe's Quartet
- Source: From Seaborn
- Structure: 3 columns -- dataset, x, y