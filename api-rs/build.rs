macro_rules! build_protos {
    ( $( $proto:literal ),+ $(,)?) => {
        tonic_build::configure().compile(&[ $( format!("./../proto/{}.proto", $proto) ),+ ], &["./../proto"]).unwrap()
    };
}

fn main() {
    build_protos![
        "ingress_controller",
        "preprocessor",
        "data_controller",
        "wiki_search",
    ]
}
