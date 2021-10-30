import os

import numpy as np
import streamlit as st

from crypto_front.crypto import (
    get_top_crypto,
    get_price_changes,
    get_token_symbol,
)

st.title("Crytpo Rocket! :rocket:")

st.markdown(
    "Want to know the top cryptos pumping right now? Select the options below and check :sunglasses: :fire:"
)

rank_top = st.select_slider(
    "Rank",
    options=np.arange(5, 100, 5).tolist(),
    value=20,
    help="Select the top number of cryptocurrencies to analyze",
)

market_cap_limit = st.select_slider(
    "Market Cap in Billions of dollars",
    options=list(range(1, 90)),
    value=1,
    help="Select cryptos with Market Cap over certain Billions of dollars",
)

timeframe = st.select_slider(
    "Time range of asset prices",
    options=list(range(1, 48)),
    value=3,
    help="Get assets prices between this time range",
)


if st.button("click to calculate!"):
    with st.spinner("Working... please wait"):
        #
        market_cap_limit = market_cap_limit * (10 ** 9)
        df = get_top_crypto(rank=rank_top, market_cap_limit=market_cap_limit)
        price_change_rank = get_price_changes(df, timeframe=timeframe)
        st.markdown("## **Here are the results!** :exploding_head:")
        st.markdown(
            f"The assets with biggest price change in the past {timeframe} hours are:"
        )
        results = []
        for index, token in enumerate(price_change_rank.items(), start=1):
            symbol = get_token_symbol(token[0])
            results.append(
                f"\n**{index}. {token[0].capitalize()}** price increased **{token[1]:.2f}%**!"
            )
        st.markdown("\n".join(results))