from backtester.features.feature import Feature


class RankFeature(Feature):

    @classmethod
    def computeForInstrument(cls, updateNum, time, featureParams, featureKey, instrumentManager):
        instrumentLookbackData = instrumentManager.getLookbackInstrumentFeatures()
        dataDf = instrumentLookbackData.getDataForFeatureForAllInstruments(featureParams['featureName'])
        return dataDf[-featureParams['period']:].rank(pct=True)

    @classmethod
    def computeForMarket(cls, updateNum, time, featureParams, featureKey, currentMarketFeatures, instrumentManager):
        lookbackDataDf = instrumentManager.getDataDf()
        data = lookbackDataDf[featureParams['featureName']]
        return data[-featureParams['period']:].rank(pct=True)
