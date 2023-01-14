from io import BufferedReader
from typing import overload, List, Union
from dataclasses import dataclass

@dataclass
class Device:
    name: str
    device_id: int
    samplerate: float

SOUND_FP = Union[str, bytes, BufferedReader]

def get_devices() -> List[Device]: ...

class Sound:
    @overload
    def __init__(self, fp: str, **kwargs) -> None: ...
    @overload
    def __init__(self, fp: bytes, **kwargs) -> None: ...
    @overload
    def __init__(self, fp: BufferedReader, **kwargs) -> None: ...

    @overload
    @staticmethod
    def from_midi(fp: str, **kwargs) -> Sound: ...
    @overload
    @staticmethod
    def from_midi(fp: bytes, **kwargs) -> Sound: ...
    @overload
    @staticmethod
    def from_midi(fp: BufferedReader, **kwargs) -> Sound: ...

    @property
    def playing(self) -> bool: ...
    @property
    def paused(self) -> bool: ...
    @property
    def samplerate(self) -> int: ...
    @property
    def duration(self) -> float: ...
    @property
    def name(self) -> str: ...
    @property
    def bit_depth(self) -> int: ...
    @property
    def bitrate(self) -> int: ...
    @property
    def channels(self) -> int: ...

    def play(self, mode: int=1) -> None: ...
    def stop(self) -> None: ...
    def pause(self) -> None: ...
    def unpause(self) -> None: ...
    def get_pos(self) -> float: ...
    def set_pos(self, value: float) -> None: ...
    def get_volume(self) -> float: ...
    def set_volume(self, value: float) -> None: ...