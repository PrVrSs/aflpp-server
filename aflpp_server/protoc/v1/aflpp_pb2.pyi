"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class StartRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BINARY_FIELD_NUMBER: builtins.int
    BINARY_ARGS_FIELD_NUMBER: builtins.int
    AFLPP_ARGS_FIELD_NUMBER: builtins.int
    SEEDS_FIELD_NUMBER: builtins.int
    binary: builtins.bytes
    binary_args: builtins.str
    aflpp_args: builtins.str
    @property
    def seeds(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bytes]: ...
    def __init__(
        self,
        *,
        binary: builtins.bytes = ...,
        binary_args: builtins.str = ...,
        aflpp_args: builtins.str = ...,
        seeds: collections.abc.Iterable[builtins.bytes] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["aflpp_args", b"aflpp_args", "binary", b"binary", "binary_args", b"binary_args", "seeds", b"seeds"]) -> None: ...

global___StartRequest = StartRequest

@typing_extensions.final
class StartResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUCCESS_FIELD_NUMBER: builtins.int
    success: builtins.bool
    def __init__(
        self,
        *,
        success: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["success", b"success"]) -> None: ...

global___StartResponse = StartResponse

@typing_extensions.final
class StatisticRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___StatisticRequest = StatisticRequest

@typing_extensions.final
class StatisticResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    START_TIME_FIELD_NUMBER: builtins.int
    LAST_UPDATE_FIELD_NUMBER: builtins.int
    RUN_TIME_FIELD_NUMBER: builtins.int
    FUZZER_PID_FIELD_NUMBER: builtins.int
    CYCLES_DONE_FIELD_NUMBER: builtins.int
    CYCLES_WO_FINDS_FIELD_NUMBER: builtins.int
    TIME_WO_FINDS_FIELD_NUMBER: builtins.int
    EXECS_DONE_FIELD_NUMBER: builtins.int
    EXECS_PER_SEC_FIELD_NUMBER: builtins.int
    EXECS_PS_LAST_MIN_FIELD_NUMBER: builtins.int
    CORPUS_COUNT_FIELD_NUMBER: builtins.int
    CORPUS_FAVORED_FIELD_NUMBER: builtins.int
    CORPUS_FOUND_FIELD_NUMBER: builtins.int
    CORPUS_IMPORTED_FIELD_NUMBER: builtins.int
    CORPUS_VARIABLE_FIELD_NUMBER: builtins.int
    MAX_DEPTH_FIELD_NUMBER: builtins.int
    CUR_ITEM_FIELD_NUMBER: builtins.int
    PENDING_FAVS_FIELD_NUMBER: builtins.int
    PENDING_TOTAL_FIELD_NUMBER: builtins.int
    STABILITY_FIELD_NUMBER: builtins.int
    BITMAP_CVG_FIELD_NUMBER: builtins.int
    SAVED_CRASHES_FIELD_NUMBER: builtins.int
    SAVED_HANGS_FIELD_NUMBER: builtins.int
    LAST_FIND_FIELD_NUMBER: builtins.int
    LAST_CRASH_FIELD_NUMBER: builtins.int
    LAST_HANG_FIELD_NUMBER: builtins.int
    EXECS_SINCE_CRASH_FIELD_NUMBER: builtins.int
    EXEC_TIMEOUT_FIELD_NUMBER: builtins.int
    SLOWEST_EXEC_MS_FIELD_NUMBER: builtins.int
    PEAK_RSS_MB_FIELD_NUMBER: builtins.int
    CPU_AFFINITY_FIELD_NUMBER: builtins.int
    EDGES_FOUND_FIELD_NUMBER: builtins.int
    TOTAL_EDGES_FIELD_NUMBER: builtins.int
    VAR_BYTE_COUNT_FIELD_NUMBER: builtins.int
    HAVOC_EXPANSION_FIELD_NUMBER: builtins.int
    AUTO_DICT_ENTRIES_FIELD_NUMBER: builtins.int
    TESTCACHE_SIZE_FIELD_NUMBER: builtins.int
    TESTCACHE_COUNT_FIELD_NUMBER: builtins.int
    TESTCACHE_EVICT_FIELD_NUMBER: builtins.int
    AFL_BANNER_FIELD_NUMBER: builtins.int
    AFL_VERSION_FIELD_NUMBER: builtins.int
    TARGET_MODE_FIELD_NUMBER: builtins.int
    COMMAND_LINE_FIELD_NUMBER: builtins.int
    start_time: builtins.int
    last_update: builtins.int
    run_time: builtins.int
    fuzzer_pid: builtins.int
    cycles_done: builtins.int
    cycles_wo_finds: builtins.int
    time_wo_finds: builtins.int
    execs_done: builtins.int
    execs_per_sec: builtins.float
    execs_ps_last_min: builtins.float
    corpus_count: builtins.int
    corpus_favored: builtins.int
    corpus_found: builtins.int
    corpus_imported: builtins.int
    corpus_variable: builtins.int
    max_depth: builtins.int
    cur_item: builtins.int
    pending_favs: builtins.int
    pending_total: builtins.int
    stability: builtins.float
    bitmap_cvg: builtins.float
    saved_crashes: builtins.int
    saved_hangs: builtins.int
    last_find: builtins.int
    last_crash: builtins.int
    last_hang: builtins.int
    execs_since_crash: builtins.int
    exec_timeout: builtins.int
    slowest_exec_ms: builtins.int
    peak_rss_mb: builtins.int
    cpu_affinity: builtins.int
    edges_found: builtins.int
    total_edges: builtins.int
    var_byte_count: builtins.int
    havoc_expansion: builtins.int
    auto_dict_entries: builtins.int
    testcache_size: builtins.int
    testcache_count: builtins.int
    testcache_evict: builtins.int
    afl_banner: builtins.str
    afl_version: builtins.str
    target_mode: builtins.str
    command_line: builtins.str
    def __init__(
        self,
        *,
        start_time: builtins.int = ...,
        last_update: builtins.int = ...,
        run_time: builtins.int = ...,
        fuzzer_pid: builtins.int = ...,
        cycles_done: builtins.int = ...,
        cycles_wo_finds: builtins.int = ...,
        time_wo_finds: builtins.int = ...,
        execs_done: builtins.int = ...,
        execs_per_sec: builtins.float = ...,
        execs_ps_last_min: builtins.float = ...,
        corpus_count: builtins.int = ...,
        corpus_favored: builtins.int = ...,
        corpus_found: builtins.int = ...,
        corpus_imported: builtins.int = ...,
        corpus_variable: builtins.int = ...,
        max_depth: builtins.int = ...,
        cur_item: builtins.int = ...,
        pending_favs: builtins.int = ...,
        pending_total: builtins.int = ...,
        stability: builtins.float = ...,
        bitmap_cvg: builtins.float = ...,
        saved_crashes: builtins.int = ...,
        saved_hangs: builtins.int = ...,
        last_find: builtins.int = ...,
        last_crash: builtins.int = ...,
        last_hang: builtins.int = ...,
        execs_since_crash: builtins.int = ...,
        exec_timeout: builtins.int = ...,
        slowest_exec_ms: builtins.int = ...,
        peak_rss_mb: builtins.int = ...,
        cpu_affinity: builtins.int = ...,
        edges_found: builtins.int = ...,
        total_edges: builtins.int = ...,
        var_byte_count: builtins.int = ...,
        havoc_expansion: builtins.int = ...,
        auto_dict_entries: builtins.int = ...,
        testcache_size: builtins.int = ...,
        testcache_count: builtins.int = ...,
        testcache_evict: builtins.int = ...,
        afl_banner: builtins.str = ...,
        afl_version: builtins.str = ...,
        target_mode: builtins.str = ...,
        command_line: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["afl_banner", b"afl_banner", "afl_version", b"afl_version", "auto_dict_entries", b"auto_dict_entries", "bitmap_cvg", b"bitmap_cvg", "command_line", b"command_line", "corpus_count", b"corpus_count", "corpus_favored", b"corpus_favored", "corpus_found", b"corpus_found", "corpus_imported", b"corpus_imported", "corpus_variable", b"corpus_variable", "cpu_affinity", b"cpu_affinity", "cur_item", b"cur_item", "cycles_done", b"cycles_done", "cycles_wo_finds", b"cycles_wo_finds", "edges_found", b"edges_found", "exec_timeout", b"exec_timeout", "execs_done", b"execs_done", "execs_per_sec", b"execs_per_sec", "execs_ps_last_min", b"execs_ps_last_min", "execs_since_crash", b"execs_since_crash", "fuzzer_pid", b"fuzzer_pid", "havoc_expansion", b"havoc_expansion", "last_crash", b"last_crash", "last_find", b"last_find", "last_hang", b"last_hang", "last_update", b"last_update", "max_depth", b"max_depth", "peak_rss_mb", b"peak_rss_mb", "pending_favs", b"pending_favs", "pending_total", b"pending_total", "run_time", b"run_time", "saved_crashes", b"saved_crashes", "saved_hangs", b"saved_hangs", "slowest_exec_ms", b"slowest_exec_ms", "stability", b"stability", "start_time", b"start_time", "target_mode", b"target_mode", "testcache_count", b"testcache_count", "testcache_evict", b"testcache_evict", "testcache_size", b"testcache_size", "time_wo_finds", b"time_wo_finds", "total_edges", b"total_edges", "var_byte_count", b"var_byte_count"]) -> None: ...

global___StatisticResponse = StatisticResponse

@typing_extensions.final
class ReportRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ReportRequest = ReportRequest

@typing_extensions.final
class ReportResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RAW_FIELD_NUMBER: builtins.int
    BUG_TYPE_FIELD_NUMBER: builtins.int
    DETAIL_FIELD_NUMBER: builtins.int
    raw: builtins.str
    bug_type: builtins.str
    detail: builtins.str
    def __init__(
        self,
        *,
        raw: builtins.str = ...,
        bug_type: builtins.str = ...,
        detail: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["bug_type", b"bug_type", "detail", b"detail", "raw", b"raw"]) -> None: ...

global___ReportResponse = ReportResponse

@typing_extensions.final
class StopRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___StopRequest = StopRequest

@typing_extensions.final
class StopResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUCCESS_FIELD_NUMBER: builtins.int
    success: builtins.bool
    def __init__(
        self,
        *,
        success: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["success", b"success"]) -> None: ...

global___StopResponse = StopResponse
