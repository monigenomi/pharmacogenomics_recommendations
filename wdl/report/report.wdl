workflow report_wf {

  call report

}

task report {

  File openpgx_json

  command <<<
    python3 /report.py -r ${openpgx_json}
  >>>

  runtime {
    docker: "monigenomi/report:1.0.0"
  }

  output {
    File recommendations_csv = "recommendations.csv"
  }
}
