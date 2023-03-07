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
    docker: "monigenomi/aldy:1.0.0"
  }

  output {
    File aldy_json = "genotypes.json"
  }
}
