import "./aldy/aldy.wdl" as aldy
import "./openpgx/openpgx.wdl" as openpgx

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

  output {
    File recommendations_json = openpgx.recommendations_json
  }
}