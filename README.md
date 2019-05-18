# Credits to Building a Blockchain by @dvf

The post on [Building a Blockchain](https://medium.com/p/117428612f46) has inspired me to work on building a more realistic and secure  blockchain on Python based on @dvf/blockchain Github (this repo is also forked from @dvf/blockchain).

Future goals will be to implement anonymous transactions - refer to Zcash shielded transactions. 

# Whats New
### Done
- Add Miner Node to periodically mine for blocks 

### In progress (in no particular order)
- Add Wallet API for users to add new transaction to node (currently use Postman to add transaction)
- Add Wallet API to calculate total amount associated per address (track address that belong to user)
- Implement broadcasting mechanism to peer nodes when new transaction added
- Fix MAX_TRANSACTIONS per block 
- Implement Secure Transactions
- Implement a persistent database to store blockchain for node
- Decreasing reward function for miners

#### Disclaimer
The repo work primarily on the Python folder (C# and Js files are forked from @dsf/blockchain)

## Installation

1. Make sure [Python 3.6+](https://www.python.org/downloads/) is installed. 
2. Install [pipenv](https://github.com/kennethreitz/pipenv). 

```
$ pip install pipenv 
```
3. Install requirements  
```
$ pipenv install 
``` 

4. Run the server:
    * `$ pipenv run python python/src/node.py` 
    * `$ pipenv run python python/src/node.py -p 5001`
    * `$ pipenv run python python/src/node.py --port 5002`
    
## Docker

Another option for running this blockchain program is to use Docker.  Follow the instructions below to create a local Docker container:

1. Clone this repository
2. Build the docker container

```
$ docker build -t blockchain .
```

3. Run the container

```
$ docker run --rm -p 80:5000 blockchain
```

4. To add more instances, vary the public port number before the colon:

```
$ docker run --rm -p 81:5000 blockchain
$ docker run --rm -p 82:5000 blockchain
$ docker run --rm -p 83:5000 blockchain
```

## Testing

1. Make sure [nose](https://nose.readthedocs.io/en/latest/) is installed.

```
$ pip install nose
```
2. Run tests
```
$ cd python
$ nosetests
``` 
You should see something like the following: 

``` 
..................................
----------------------------------------------------------------------
Ran 8 tests in 0.440s

OK
``` 

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request/Issue.

