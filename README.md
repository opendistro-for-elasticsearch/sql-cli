# Open Distro for Elasticsearch SQL CLI

The SQL CLI component in Open Distro for Elasticsearch (ODFE) is a stand-alone Python application and can be launched by a 'wake' word `odfesql`. It serves as a support only for 
[Open Distro SQL plugin for Elasticsearch](https://opendistro.github.io/for-elasticsearch-docs/docs/sql/). User must have the  ODFE SQL plugin installed to your Elasticsearch instance to connect. Users can run this CLI from MacOS and Linux, and connect to any valid Elasticsearch end-point such as Amazon Elasticsearch.

## Installation
- `pip install odfesql` 
- ODFE SQL CLI is only compatible with Python 3, because Python 2 is no longer maintained since 01/01/2020. See https://pythonclock.org/ 

## Configuration
- A config file is automatically created at `~/.config/odfesql-cli/config` at first launch (for MacOS and Linux). 
Check out [clirc](src/conf/clirc) for details of all available configurations.
- It can be configured and will be auto-loaded next time.

## Features
- Multi-line input
- Input auto-completion with index suggestions
- Syntax highlighting
- Formatted output
    - Tabular format
    - Fields name with color
    - Enable horizontal display (by default) and vertical display when output is too wide, for better visualization
    - Pagination for long output

- Connect to Elasticsearch with/without security enabled on either **Elasticsearch OSS or Amazon Elasticsearch domains**.
- Load config file

## Basic Usage
- ![](./screenshots/usage.gif)
- The CLI supports all types of query that ODFE SQL supports. Refer to [ODFE SQL basic usage](https://github.com/opendistro-for-elasticsearch/sql#basic-usage)
    
- Configurable connection properties
    - *endpoint:* no need to specify an option, anything follow by launch word `odfesql` is regarded as the endpoint. 
    If user doesn't provide an endpoint, by default it will try to connect to http://localhost:9200
    - *-u/-w:* username and password. User needs to provide credentials when connecting to:
        - Elasticsearch with X-pack security enabled
        - Elasticsearch OSS with [Open Distro Security Plugin](https://opendistro.github.io/for-elasticsearch-docs/docs/install/plugins/) installed
        - Amazon Elasticsearch domain with [Fine Grained Access Control](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/fgac.html) enabled

    - *--aws-auth:* turn on to use AWS sigV4 authentication. It can be configured by AWS CLI `aws configure` command. ODFE SQL
    CLI will try to retrieve this config to connect.

- Run single query from command line with options
    - *--help:* help page for options
    - *-q:* follow by a single query
    - *-f:* support *jdbc/raw* format output
    - *-v:* display data vertically
    - *-e:* translate sql to DSL

- Run the CLI with options
    - *-p*: always use pager to display output
    - *--clirc*: provide path of config file to load


## Code of Conduct

This project has adopted an [Open Source Code of Conduct](https://opendistro.github.io/for-elasticsearch/codeofconduct.html).


## Security issue notifications

If you discover a potential security issue in this project we ask that you notify AWS/Amazon Security 
via our [vulnerability reporting page](http://aws.amazon.com/security/vulnerability-reporting/). 
Please do **not** create a public GitHub issue.


## Licensing

See the [LICENSE](./LICENSE.TXT) file for our project's licensing. We will ask you to confirm the licensing of your contribution.


## Copyright

Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
