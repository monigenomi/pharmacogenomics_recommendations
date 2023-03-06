workflow aldy_wf {

  call aldy

}

task aldy {

  File bam
  File bai

  command <<<
    python3 /aldy.py --bam ${bam}
  >>>

  runtime {
    docker: "aldy:latest"
  }

  output {
    File aldy_json = "genotypes.json"
  }
}
