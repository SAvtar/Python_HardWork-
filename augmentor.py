import Augmentor

path_to_data = "/mnt/745AA3875AA34528/SOFTWARES/currency-detector-opencv-master/dataset/ten"   #/home/user/images/dataset1/  D:\\tmp\Data Augmentor\\50\\fron

# Create a pipeline
p = Augmentor.Pipeline(path_to_data)

# Add some operations to an existing pipeline.

# First, we add a horizontal flip operation to the pipeline:
p.flip_left_right(probability=0.4)

# Now we add a vertical flip operation to the pipeline:
p.flip_top_bottom(probability=0.8)

# Now we add a vertical flip operation to the pipeline:
p.flip_random(probability=0.8)

# Add a rotate90 operation to the pipeline:
p.rotate90(probability=0.1)

# Add a shear
p.shear(probability=1, max_shear_right=15, max_shear_left=14)
p.shear(probability=1, max_shear_left=15, max_shear_right=14)

# Add a skew
p.skew(probability=1)

# Add random distortion
p.random_distortion(probability=0.8, grid_height=16, grid_width=16, magnitude=8)

# Here we sample 100,000 images from the pipeline.

# It is often useful to use scientific notation for specify
# large numbers with trailing zeros.
num_of_samples = int(2000)    # This is generating 4000 if it'd 've been 1e5 then it'd 've been 100000 images

# Now we can sample from the pipeline:
p.sample(num_of_samples)
