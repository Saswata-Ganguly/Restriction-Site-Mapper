import argparse

def find_restriction_sites(dna_sequence, length):
    restriction_sites = []
    for i in range(len(dna_sequence) - length + 1):
        subsequence = dna_sequence[i:i+length]
        if subsequence == subsequence[::-1]:
            restriction_sites.append(subsequence)
    return restriction_sites

def main():
    parser = argparse.ArgumentParser(description="Find restriction sites in a DNA sequence.")
    parser.add_argument("sequence", type=str, help="DNA sequence string")
    parser.add_argument("length", type=int, help="Length of restriction sites to find")
    args = parser.parse_args()

    restriction_sites = find_restriction_sites(args.sequence, args.length)
    
    print(f"Restriction sites of length {args.length} in the sequence:")
    for restriction_site in restriction_sites:
        print(restriction_site)
