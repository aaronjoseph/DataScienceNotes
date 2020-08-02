Although Scikit-Learn provides many useful transformers, you will need to write
your own for tasks such as custom cleanup operations or combining specific
attributes. You will want your transformer to work seamlessly with Scikit-Learn functionalities (such as pipelines), and since Scikit-Learn relies on duck typing (not inheritance), all you need to do is create a class and implement three methods: fit()
(returning self ), transform() , and fit_transform() 

You can get the last one for free by simply adding TransformerMixin as a base class. If you add BaseEstimator as a base class (and avoid args and kargs in your constructor), you will also get two extra methods ( get_params() and set_params() ) that will be useful for automatic `hyperparameter tuning`

