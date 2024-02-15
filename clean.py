import pandas as pd


def clean(input1, input2, output):
    # (1) merge the two input data files (i.e., respondent_contact.csv, respondent_other.csv)
    # based on the ID value.
    contact = pd.read_csv(input1)
    other = pd.read_csv(input2)
    merge = pd.merge(contact, other, left_on='respondent_id', right_on='id')
    merge = merge.drop('id', axis=1)
    # (2) drop any rows with missing values
    merge = merge.dropna()
    # (3) drop any rows if their job value contains ‘insurance’ or ‘Insurance’
    merge = merge[~merge['job'].str.contains('insurance|Insurance')]
    # (4) save the cleaned data in project folder. The file name will need to specified by the
    # positional argument output.
    merge.to_csv(output, index=False)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input1', help='respondent_contact.csv')
    parser.add_argument('input2', help='respondent_other.csv')
    parser.add_argument('output', help='Output_file.csv')
    args = parser.parse_args()

    clean(args.input1, args.input2, args.output)

    cleaned = pd.read_csv(args.output)
    print("Shape of the output file:", cleaned.shape)