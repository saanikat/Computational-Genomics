#!/usr/bin/env python3

import subprocess
import pathlib
import os
import glob


# Change this to the directory where the assembly results are, without the trailing "/"
contig_dir = 'assembly/final_results/*'

pathlib.Path('comparative/').mkdir(exist_ok=True)
os.chdir('comparative/')
input_filenames = [x.split('/')[-1] for x in glob.glob(f'../{contig_dir}/*.fasta')]
contig_ids = [x.split("/")[-1].split("_")[0] for x in input_filenames] #extracting the contig ids


def run_fastani():
    assemblies = glob.glob('../FastANI/data/*.fasta')

    # Uncomment the following line to print the number of assemblies found
    # print(len(assemblies))

    for i in range(len(assemblies)):
        for j in range(i + 1, len(assemblies)):
            print(f"{assemblies[i]} and {assemblies[j]} being compared...")
            output_file = f"/home/team1/comparative/FastANI/FastANI_Outdir/FastANI_Outdir_{assemblies[i].split('/')[-1]}_{assemblies[j].split('/')[-1]}.txt"
            subprocess.run(["fastANI", "-q", assemblies[i], "-r", assemblies[j], "-o", output_file])

    output_files = glob.glob("/home/team1/comparative/FastANI/FastANI_Outdir/FastANI_Outdir_*.txt")
    with open("resultsFastANI.txt", "w") as outfile:
        for output_file in output_files:
            with open(output_file) as infile:
                outfile.write(f"{infile.readline().strip()}\n")
              
def run_ANIclustermap(input_dir, output_dir, fig_width=20, fig_height=15, annotation=False):
    args = ['ANIclustermap', '-i', input_dir, '-o', output_dir, '--fig_width', str(fig_width), '--fig_height', str(fig_height)]
    if annotation:
        args.append('--annotation')
    subprocess.run(args)


def run_skANI():
    
    genomes = glob.glob('../skANI/data/*.fasta')

    # Uncomment the following line to print the number of genomes found
    # print(len(genomes))

    for i in range(len(genomes)):
        for j in range(i+1, len(genomes)):
            print(f"Comparing {genomes[i]} and {genomes[j]}...")
            output_file = f"/home/team1/comparative/skANI/SKANI_Outdir/SKANI_Outdir_{genomes[i].split('/')[-1]}_{genomes[j].split('/')[-1]}.txt"
            subprocess.run(["skani", "dist", genomes[i], genomes[j], "-t", "5", "-o", output_file])
  
     # construct distance matrix for all genomes in folder
    subprocess.run(['skani', 'triangle', '/home/team1/comparative/skANI/data/genome_folder/*', '>', '../skANI/skani_ani_matrix.txt'], shell=True)

    # run clustering/visualization script
    subprocess.run(['python', '/home/team1/comparative/skANI/clustermap_triangle.py', '../skANI/skani_ani_matrix.txt'])

def run_mlst():
    pathlib.Path('mlst_output/').mkdir(exist_ok=True)
    os.chdir('mlst_output/')
    output_file='/home/team1/comparative/mlst/mlst_output/mlst.tsv' #change this to the path of your desired output directory
    p=subprocess.Popen(['mlst',contig_dir,'>',output_file])


def run_parsnp():
    pathlib.Path('parsnp_output/').mkdir(exist_ok=True)
    os.chdir('parsnp_output/')
    output_dir='/home/team1/comparative/snp_analysis/parsnp_output/' #change this to the path of your desired output directory
    p=subprocess.Popen(['parsnp','-g','/home/team1/comparative/snp_analysis/ref/sequence.gbk','-d',contig_dir,'-c','-o',output_dir])

if __name__ == "__main__":
    run_fastani()
    run_ANIclustermap()
    run_skANI()
    run_mlst()
    run_parsnp()
    
