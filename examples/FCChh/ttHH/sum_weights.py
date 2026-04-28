import ROOT
import os

# Path to the directory containing the ROOT files
directory = "outputs/FCChh/ttHH/"

# List all ROOT files in the directory
root_files = [f for f in os.listdir(directory) if f.endswith(".root")]

# Loop over all ROOT files
for filename in root_files:
    filepath = os.path.join(directory, filename)
    file = ROOT.TFile.Open(filepath)

    if not file or file.IsZombie():
        print(f"Could not open file: {filename}")
        continue

    # Get the sum of weights from the TParameter<float>
    sum_of_weights = file.Get("SumOfWeights")

    if sum_of_weights:
        print(f"{filename}: Sum of Weights = {sum_of_weights.GetVal()}")
    else:
        print(f"{filename}: SumOfWeights not found")

    file.Close()
