select *
    from "FICO_customer_information_copy" "customers"
    left join "FICO_loan_request_copy" "requests"
    on "customers"."id" = "requests"."id"

