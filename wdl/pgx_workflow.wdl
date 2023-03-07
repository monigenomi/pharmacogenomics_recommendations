import "./aldy/aldy.wdl" as aldy
import "./openpgx/openpgx.wdl" as openpgx
import "./report/report.wdl" as report

workflow pgx_workflow {

  File bam
  File bai

  call aldy.aldy {
    input:
      bam = bam,
      bai = bai
  }

  call openpgx.openpgx {
    input:
      genotypes_json = aldy.aldy_json
  }

  call report.report {
    input:
      openpgx_json = openpgx.recommendations_json
  }

  output {
    File recommendations_csv = report.recommendations_csv
    File recommendations_json = openpgx.recommendations_json
  }
}