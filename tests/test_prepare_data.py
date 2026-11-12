from sklearn.datasets import load_iris
 
def test_dummy():
df = load_iris(as_frame=True).frame
assert len(df) == 150