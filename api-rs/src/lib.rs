use ::unstringify::unstringify;
macro_rules! define_proto {
    ( $($proto_s:literal),+ $(,)?) => (
        $( unstringify!(let $proto = unstringify!($proto_s) in {
            pub mod $proto {
               ::tonic::include_proto!($proto_s);
            }
        }); )+
)}

define_proto![
    "ingress_controller",
    "preprocessor",
    "index_updater",
    "url_metadata",
];
