import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import the dataset
# It has to be the exact path to the file on your system. Adjust as necessary.
#df = pd.read_csv("it_nasa_http_july1995.csv")
df = pd.read_csv(r"C:\Users\...\...\it_nasa_http_july1995.csv")

# Select the response-size column and remove missing values
bytes_data = df["bytes"].dropna()

########### Remove zero values from the dataset ###########
#bytes_data = bytes_data[bytes_data > 0]


# Display basic statistics
print("Number of valid observations:", len(bytes_data))
print("Sample median:", bytes_data.median())
print("Sample mean:", bytes_data.mean())
print("Sample mode:", bytes_data.mode())
print("Maximum value:", df["bytes"].max())


# Bootstrap confidence interval for the median
sample = bytes_data.sample(
    n=5000,
    random_state=42
).to_numpy()

rng = np.random.default_rng(42)
bootstrap_medians = []

for _ in range(2000):
    bootstrap_sample = rng.choice(
        sample,
        size=len(sample),
        replace=True
    )
    bootstrap_medians.append(
        np.median(bootstrap_sample)
    )

# Calculate 95% bootstrap CI
lower_ci, upper_ci = np.percentile(
    bootstrap_medians,
    [2.5, 97.5] # 95 percentile confidence interval 
)

print("\nBootstrap Results")
print("")
print(f"Sample median: {np.median(sample):,.2f} bytes")
print(f"95% Bootstrap CI: ({lower_ci:,.2f}, {upper_ci:,.2f}) bytes")


#counts, bin_edges = np.histogram(bytes_data, bins=20)
#max_bin_index = np.argmax(counts)
#max_bin_center = (bin_edges[max_bin_index] + bin_edges[max_bin_index + 1]) / 2
#print(f"X-axis value (bin center) with largest count: {max_bin_center}")

# Create histogram
plt.figure(figsize=(10, 6))
plt.hist(bytes_data, bins=50, edgecolor="black", color="steelblue")

# Set Y-axis to logarithmic scale
plt.yscale("log")
plt.yticks(
    [1, 10, 100, 1000, 10000, 100000, 1000000],
    ["1", "10", "100", "1,000", "10,000", "100,000", "1,000,000"]
)

############### X-axis looks messed up with log scale ###############
# Set X-axis to logarithmic scale
#plt.xscale("log")
#plt.xticks(
#    [10, 100, 1000, 10000, 100000, 1000000, 10000000],
#    ["10", "100", "1,000", "10,000", "100,000", "1,000,000", "10,000,000"]
#)

############### Histogram intervals marked begin ###############
# Mark that median on the histogram (red)
median_value = bytes_data.median()
plt.axvline(
    median_value,
    color="red",
    linestyle="--",
    linewidth=2,
    label=f"Median = {median_value:,.0f} bytes"
)

# Mark that mean on the histogram (blue)
mean_value = bytes_data.mean()
plt.axvline(
    mean_value,
    color="blue",
    linestyle="--",
    linewidth=2,
    label=f"Mean = {mean_value:,.0f} bytes"
)

# Mark that mode on the histogram (green)
mode_value = bytes_data.mode()[0]
plt.axvline(
    mode_value,
    color="green",
    linestyle="--",
    linewidth=2,
    label=f"Mode = {mode_value:,.0f} bytes"
)

lower_ci_value = lower_ci
plt.axvline(
    lower_ci_value,
    color="orange",
    linestyle="--",
    linewidth=2,
    label=f"Lower CI = {lower_ci_value:,.0f} bytes"
)

upper_ci_value = upper_ci
plt.axvline(
    upper_ci_value,
    color="purple",
    linestyle="--",
    linewidth=2,
    label=f"Upper CI = {upper_ci_value:,.0f} bytes"
)
############### Histogram intervals marked end ###############


plt.xlabel("Response Size (bytes)")
plt.ylabel("Frequency")
plt.title("NASA HTTP Server Log: Response Sizes (July 1995)")
plt.legend()
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()

