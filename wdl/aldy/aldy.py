import subprocess
import csv
import json
from argparse import ArgumentParser
import os


def run_aldy_for_gene(gene: str, bam_path: str) -> str:
    try:
        run_aldy = subprocess.run([
            "aldy",
            "genotype",
            "-p", "illumina",
            "-g", gene,
            "-o", f"{gene}.aldy",
            bam_path          
        ], check=True, capture_output=True)

        print(run_aldy.stdout.decode())
        print(run_aldy.stderr.decode())
        return f"{gene}.aldy"
    except subprocess.CalledProcessError as e:
        print(e.stderr.decode())
    pass


GENES = [
      'CYP1A1', 'CYP1A2', 'CYP2A13', 'CYP2A6', 'CYP2B6', 'CYP2C19', 'CYP2C8',
      'CYP2C9', 'CYP2D6', 'CYP2E1', 'CYP2F1', 'CYP2J2', 'CYP2R1', 'CYP2S1',
      'CYP2W1', 'CYP3A4', 'CYP3A43', 'CYP3A5', 'CYP3A7', 'CYP4F2', 'CYP4F2',
      'DPYD', 'G6PD', 'NUDT15', 'SLCO1B1', 'TPMT'
      ]


def genotype_genes(bam_path: str, genes=GENES) -> list:
    results = []
    for gene in genes:
        aldy_file = run_aldy_for_gene(gene, bam_path)
        results.append(aldy_file)
    return results


def get_result_from_aldy_file(aldy_file_path: str) -> dict:
    with open(aldy_file_path) as csvfile:
      csv_content = csv.reader(csvfile, delimiter="\t", quotechar='|')
      next(csv_content)
      next(csv_content) # skip the headers
      for row in csv_content:
        # Take first solution
        gene = row[1]
        genotype = row[3]
        break
    return gene, genotype


def create_openpgx_input_dict(aldy_files: list) -> dict:
    result = {}
    # Each aldy file represents gene and its genotyping results if Aldy have found something
    for aldy_file in aldy_files:
        if os.stat(aldy_file).st_size == 0:
          print(f"{aldy_file} is empty, skipped...")
          continue
        gene, genotype = get_result_from_aldy_file(aldy_file)
        result[gene] = genotype
    return result
    

def create_openpgx_json(merged_results: dict):
    with open("./genotypes.json", "w") as file:
        json.dump(merged_results, file, indent=2)


def main():
    parser = ArgumentParser()
    parser.add_argument("-b", "--bam")
    parser.add_argument("-o", "--output")
    args = vars(parser.parse_args())

    # 1. First run aldy genotype in look for all implemented genes and write results to separated files <{gene}.aldy>
    aldy_files = genotype_genes(args["bam"])

    # 2. Create dictionary with all genes and genotypes
    openpgx_dictionary = create_openpgx_input_dict(aldy_files)

    # 3. Save to json
    create_openpgx_json(openpgx_dictionary)


if __name__ == "__main__":
    main()
    