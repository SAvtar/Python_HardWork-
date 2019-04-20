import Augmentor
def applyAug(myVar, our_probability=0.8, our_sample=50):
	myVar.rotate(probability=our_probability, max_left_rotation=5, max_right_rotation=5)
	myVar.skew_tilt(probability=our_probability, magnitude=0.8)
	myVar.random_erasing(probability=our_probability, rectangle_area=0.2)
	myVar.sample(our_sample)
	return;

def applyAugOnlyErase(myVar, our_probability=0.9, our_sample=50):
	myVar.random_erasing(probability=our_probability, rectangle_area=0.35)
	myVar.sample(our_sample)
	return;


fifty = Augmentor.Pipeline("/Users/shwetank/Documents/code/Datasets/testcurrency/fifty")
ten   = Augmentor.Pipeline("/Users/shwetank/Documents/code/Datasets/testcurrency/ten")

applyAug(fifty, our_probability=1.0, our_sample=50)
applyAug(ten, our_probability=0.5, our_sample=100)