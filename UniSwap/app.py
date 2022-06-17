import requests
import streamlit as st
# pretty print is used to print the output in the console in an easy to read format
from pprint import pprint


# function to use requests.post to make an API call to the subgraph url
def run_query(q):

    # endpoint where you are making the request
    request = requests.post('https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3'
                            '',
                            json={'query': query})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Query failed. return code is {}.      {}'.format(request.status_code, query))


# The Graph query - Query pools
query = """

{
pools(orderBy: totalValueLockedETH, orderDirection: desc) {
    id
    token0 {
        id
        symbol
        name
        decimals
    }
    token1 {
        id
        symbol
        name
        decimals
    }
    feeTier
    liquidity
    token0Price
    token1Price
    totalValueLockedETH
    volumeUSD
  }
}
"""



result = run_query(query)
# col1, col2, col3 = st.columns(3)


for pool in result['data']['pools']:
    st.title('Pool ID')
    st.write(pool['id'])
    st.caption("Token0 Address")
    # st.write(pool['token0'])
    st.write(pool['token0']['id'])
    st.write(pool['token0']['symbol'])
    st.write(pool['token0']['name'])
    st.caption("decimals")
    st.write(pool['token0']['decimals'])
    st.caption("Token1 Address")
    # st.write(pool['token1'])
    st.write(pool['token1']['id'])
    st.write(pool['token1']['symbol'])
    st.write(pool['token1']['name'])
    st.caption("decimals")
    st.write(pool['token1']['decimals'])
    st.caption("Fee")
    st.write(pool['feeTier'])
    st.caption("Liquidity")
    st.write(pool['liquidity'])
    st.caption("Token0 Price")
    st.write(pool['token0Price'])
    st.caption("Token1 Price")
    st.write(pool['token1Price'])
    st.caption("TVL in ETH")
    st.write(pool['totalValueLockedETH'])
    st.caption("Volume in USD")
    st.write(pool['volumeUSD'])
# st.write(result)