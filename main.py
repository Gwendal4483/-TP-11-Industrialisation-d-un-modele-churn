import src.data as data
import src.evaluate as evaluate
import src.preprocessing as preprocessing
import src.train as train

if __name__ == "__main__":
    df = data.load_data("data/churn.csv")
    print(df.head())
    df = preprocessing.preprocess(df)
    model, X_test, y_test = train.train_model(df)
    evaluate.evaluate(model, X_test, y_test)
    