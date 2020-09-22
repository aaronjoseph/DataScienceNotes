Statistical Analysis that can be done in time series are
- Maximum
- Minimum
- Average
- Moving Average
- Variance
- Co-variance
- Standard Deviation
- Autocorrelation

---
### [[Sequence Models]] used in Time-Series
- [[RNN]] were created to tackle the sparsity, inefficiency, and lack of information with traditional n-gram and BoW methods by passing the previous outputinto the next input, creating a more sequential approach towards modelling
- LSTM's were created to address problems of RNNs forgetting inputs more than a few time steps away by introducing long-term and short-term memory channels, controlled by gates
- Some downsides of [[LSTM]]'s include unfriendliness towards transfer learning, unusable for parallel computing, and a limited attention span, even afer being expanded
- [[Transformers]] throw away recursive modelling. Instead, with attention matrices, transformers are able to directly access other elements of the output, which allow them to have infinite attention sizes. Additionally, they can run on parallel computing