from datasource.repository.game_storage import GameStorage
from datasource.repository.service_impl_repo import ServiceImplDs, Repository
from domain.service.service_impl import ServiceImpl

class Container:
    def __init__(self):
        self.storage: GameStorage | None = None
        self.repository: Repository | None = None
        self.repo_service: ServiceImplDs | None = None
        self.service: ServiceImpl | None = None
        self._init_dependencies()

    def get_service(self) -> ServiceImpl:
        assert self.service is not None
        return self.service
    
    def get_repo_service(self) -> ServiceImplDs:
        assert self.repo_service is not None
        return self.repo_service
    
    def get_repository(self) -> Repository:
        assert self.repository is not None
        return self.repository
        
    def _init_dependencies(self) -> None:
        self._init_storage()
        self._init_repo()
        self._init_service()
        self._init_repo_service()

    def _init_storage(self) -> None:
        if self.storage is None:
            self.storage = GameStorage()

    def _init_repo(self) -> None:
        if self.repository is None:
            assert self.storage is not None
            self.repository = Repository(self.storage)

    def _init_repo_service(self) -> None:
        if self.repo_service is None:
            assert self.repository is not None
            assert self.service is not None
            self.repo_service = ServiceImplDs(self.repository, self.service)

    def _init_service(self) -> None:
        if self.service is None:
            self.service = ServiceImpl()

container_instance = Container()

def get_container() -> Container:
    return container_instance