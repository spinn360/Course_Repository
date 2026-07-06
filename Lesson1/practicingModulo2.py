total_zip_ties = 250
bundle_size = 12

# Write the math for these two variables
full_bundles = total_zip_ties // bundle_size
loose_ties = total_zip_ties % bundle_size

print(f'Full Bundles: {full_bundles} Loose Ties: {loose_ties}')