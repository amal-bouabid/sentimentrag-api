from app.sentiment_analysis.analyzer import SentimentAnalyzer

def test_sentiment_positive():
    analyzer = SentimentAnalyzer.get_instance()
    result = analyzer.analyze("This is a fantastic product!")
    assert result["sentiment"] == "POSITIVE"
    assert 0.5 < result["score"] <= 1

def test_sentiment_negative():
    analyzer = SentimentAnalyzer.get_instance()
    result = analyzer.analyze("This is the worst service ever.")
    assert result["sentiment"] == "NEGATIVE"
    assert 0.5 < result["score"] <= 1

def test_sentiment_neutral_or_fallback():
    analyzer = SentimentAnalyzer.get_instance()
    result = analyzer.analyze("")  # Cas vide
    assert "sentiment" in result
    assert "score" in result
    assert isinstance(result["score"], float)
