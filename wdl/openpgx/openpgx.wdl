workflow openpgx_wf {

  call openpgx

}

task openpgx {

  File genotypes_json

  command <<<
    set -e -o pipefail
    openpgx ${genotypes_json} -o "recommendations.json"
  >>>

  runtime {
    docker: "monigenomi/openpgx:1.0.0"
  }

  output {
    File recommendations_json = "recommendations.json"
  }
}
